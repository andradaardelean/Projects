using TaskService.WebApi.Settings;

namespace TaskService.WebApi
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
            services.SetupDonationClient(settingsProvider);
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

            // Web sockets middleware
            app.UseCors(x => x
                .AllowAnyMethod()
                .AllowAnyHeader()
                .SetIsOriginAllowed(origin => true) // allow any origin
                .AllowCredentials()); // allow credentials

            app.UseWebSockets();
            app.UseRouting();
            app.UseAuthentication();
            app.UseAuthorization();

            app.UseEndpoints(endpoints =>
            {
                endpoints.MapControllers();
            });


            // LIVE ON: http://localhost:12800/task/swagger/index.html
            app.UseSwagger(options =>
            {
                options.RouteTemplate = "task/swagger/{documentName}/task.json";
            });
            app.UseSwaggerUI(
                options =>
                {
                    options.RoutePrefix = "task/swagger";
                    options.SwaggerEndpoint("v1/task.json", "Task Service");
                });
        }
    }
}
