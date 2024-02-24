using Location.WebApi.Services;
using LocationService.DataStore;
using LocationService.DataStore.Mongo;
using LocationService.WebApi.Controllers;
using LocationService.WebApi.Services;
using LocationService.WebApi.Settings;
using Microsoft.OpenApi.Models;
using OpenTelemetry.Resources;
using OpenTelemetry.Trace;
using System.Diagnostics;

namespace LocationService.WebApi
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
                    Title = "Location Service",
                    Description = "This is the location Service.",
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
            var dataProvider = new MongoDataProvider(mongoDataContext, settingsProvider.LocationCollection);

            services.AddSingleton<IDataProvider>(dataProvider);
            return services;
        }

        public static IServiceCollection SetupTelemetry(this IServiceCollection services, ISettingsProvider settingsProvider)
        {
            services.AddOpenTelemetryTracing(builder =>
            {
                builder.AddAspNetCoreInstrumentation()
                    .AddHttpClientInstrumentation()
                    .AddSource(nameof(LocationController))
                    .SetResourceBuilder(ResourceBuilder.CreateDefault().AddService("Location Service"))
                    .AddJaegerExporter();
            });
            ActivitySource source = new ActivitySource(nameof(LocationController));
            IServiceCollection serviceCollection = services.AddSingleton<ActivitySource>(source);
            return services;
        }

        public static IServiceCollection SetupFacade(this IServiceCollection services)
        {
            services.AddSingleton<ILocationFacade, LocationFacade>();
            return services;
        }
    }
}
