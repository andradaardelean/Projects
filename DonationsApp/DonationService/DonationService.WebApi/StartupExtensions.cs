using DonationService.WebApi.Services;
using DonationService.DataStore;
using DonationService.DataStore.Mongo;
using DonationService.WebApi.Services;
using DonationService.WebApi.Settings;
using Microsoft.OpenApi.Models;
using DonationService.WebApi.Controllers;
using OpenTelemetry.Trace;
using OpenTelemetry.Resources;
using System.Diagnostics;
using DonationService.Clients.Donation;
using DonationService.Clients;

namespace DonationService.WebApi
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
                    Title = "Donation Service",
                    Description = "This is the donation Service.",
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
            var dataProvider = new MongoDataProvider(mongoDataContext, settingsProvider.DonationCollection);

            services.AddSingleton<IDataProvider>(dataProvider);
            return services;
        }

        public static IServiceCollection SetupTelemetry(this IServiceCollection services, ISettingsProvider settingsProvider)
        {
            services.AddOpenTelemetryTracing(builder =>
            {
                builder.AddAspNetCoreInstrumentation()
                    .AddHttpClientInstrumentation()
                    .AddSource(nameof(DonationController))
                    .SetResourceBuilder(ResourceBuilder.CreateDefault().AddService("Donation Service"))
                    .AddJaegerExporter();
            });
            ActivitySource source = new ActivitySource(nameof(DonationController));
            IServiceCollection serviceCollection = services.AddSingleton<ActivitySource>(source);
            return services;
        }

        public static IServiceCollection SetupFacade(this IServiceCollection services)
        {
            services.AddSingleton<IDonationFacade, DonationFacade>();
            return services;
        }

        public static IServiceCollection SetupTaskClient(this IServiceCollection services, ISettingsProvider settingsProvider)
        {
            var taskClient = new TaskClient(settingsProvider.TaskServiceUrl);
            services.AddSingleton<ITaskClient>(taskClient);
            return services;
        }
    }
}
