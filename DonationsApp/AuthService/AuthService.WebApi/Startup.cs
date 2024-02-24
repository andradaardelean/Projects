using AuthService.WebApi.Settings;
using Microsoft.Extensions.Options;
using Microsoft.Win32.SafeHandles;

namespace AuthService.WebApi
{
    public class Startup
    {
        public IConfiguration Configuration { get; }

        public Startup(IConfiguration configuration)
        {
            Configuration = configuration;
        }
        public void ConfigureServices(IServiceCollection services)
        {
            //Add all:
            ISettingsProvider settingsProvider = services.SetupSettings();
            services.SetupTelemetry(settingsProvider);
            services.SetupSwagger();
            services.SetupMongo(settingsProvider);
            services.SetupFacade();
            services.AddCors();

            services.AddControllers(options =>
            {
                options.AllowEmptyInputInBodyModelBinding = true;
            });
        }

        // This method gets called by the runtime. Use this method to configure the HTTP request pipeline.
        public void Configure(IApplicationBuilder app, IWebHostEnvironment env)
        {
            if (env.IsDevelopment())
            {
                app.UseDeveloperExceptionPage();
            }

            var origins = new List<string>();
            origins.Add("http://localhost:8083");
            origins.Add("http://swagger-ui:8083");
            origins.Add("http://localhost:3000");
            origins.Add("http://localhost:12500");
            origins.Add("http://authservice:12500");

            app.UseCors(x => x
                .AllowAnyHeader()
                .AllowCredentials()
                .AllowAnyMethod()
                .WithOrigins(origins.ToArray())); // allow credentials

            app.UseCors();

            app.UseWebSockets();
            app.UseRouting();
            app.UseAuthentication();
            app.UseAuthorization();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });


            // LIVE ON: http://localhost:12500/auth/swagger/index.html
            app.UseSwagger(options =>
            {
                options.RouteTemplate = "auth/swagger/{documentName}/auth.json";
            });
            app.UseSwaggerUI(
                options =>
                {
                    options.RoutePrefix = "auth/swagger";
                    options.SwaggerEndpoint("v1/auth.json", "Auth Service");
                });
        }
    }
}
