using AuthService.DataStore;
using AuthService.DataStore.Mongo;
using AuthService.WebApi.Controllers;
using AuthService.WebApi.Services;
using AuthService.WebApi.Settings;
using Microsoft.OpenApi.Models;
using OpenTelemetry.Exporter;
using OpenTelemetry.Metrics;
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;
using System.Diagnostics;
using System.Runtime.CompilerServices;

namespace AuthService.WebApi
{
    internal static class StartupExtensions
    {
        public static ISettingsProvider SetupSettings(this IServiceCollection services)
        {
            ISettingsProvider settingsProvider = SettingsProviderFactory.Create();
            services.AddSingleton<ISettingsProvider>(settingsProvider);
            return settingsProvider;
        }

        public static IServiceCollection SetupSwagger(this IServiceCollection services)
        {
            services.AddSwaggerGen(options =>
            {
                options.SwaggerDoc("v1", new OpenApiInfo
                {
                    Version = "1",
                    Title = "Auth Service",
                    Description = "This is the auth Service.",
                    Contact = new OpenApiContact
                    {
                        Name = "Catalin",
                        Email = "catalinbgnr@gmail.com"
                    }
                });
            });
            return services;
        }

        public static IServiceCollection SetupMongo(this IServiceCollection services, ISettingsProvider settingsProvider)
        {
            var mongoDataContext = new MongoDataContext(settingsProvider.ConnectionString);
            var dataProvider = new MongoDataProvider(mongoDataContext, settingsProvider.UserCollection);

            services.AddSingleton<IDataProvider>(dataProvider);
            return services;
        }

        public static IServiceCollection SetupTelemetry(this IServiceCollection services, ISettingsProvider settingsProvider)
        {
            services.AddOpenTelemetryTracing(builder =>
            {
                builder.AddAspNetCoreInstrumentation()
                    .AddHttpClientInstrumentation()
                    .AddSource(nameof(AuthController))
                    .SetResourceBuilder(ResourceBuilder.CreateDefault().AddService("Auth Service"))
                    .AddJaegerExporter(options =>
                    {
                    });
            });
            ActivitySource source = new ActivitySource(nameof(AuthController));
            IServiceCollection serviceCollection = services.AddSingleton<ActivitySource>(source);
            return services;
        }

        public static IServiceCollection SetupFacade(this IServiceCollection services)
        {
            services.AddSingleton<IAuthFacade, AuthFacade>();
            return services;
        }
    }
}
