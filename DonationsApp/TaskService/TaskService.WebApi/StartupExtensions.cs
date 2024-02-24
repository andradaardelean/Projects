using TaskService.WebApi.Services;
using TaskService.DataStore;
using TaskService.DataStore.Mongo;
using TaskService.WebApi.Settings;
using Microsoft.OpenApi.Models;
using TaskService.WebApi.Controllers;
using OpenTelemetry.Trace;
using OpenTelemetry.Resources;
using System.Diagnostics;
using TaskService.Clients;

namespace TaskService.WebApi
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
                    Title = "Task Service",
                    Description = "This is the task Service.",
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
            var dataProvider = new MongoDataProvider(mongoDataContext, settingsProvider.TaskCollection);

            services.AddSingleton<IDataProvider>(dataProvider);
            return services;
        }

        public static IServiceCollection SetupTelemetry(this IServiceCollection services, ISettingsProvider settingsProvider)
        {
            services.AddOpenTelemetryTracing(builder =>
            {
                builder.AddAspNetCoreInstrumentation()
                    .AddHttpClientInstrumentation()
                    .AddSource(nameof(TaskController))
                    .SetResourceBuilder(ResourceBuilder.CreateDefault().AddService("Task Service"))
                    .AddJaegerExporter();
            });
            ActivitySource source = new ActivitySource(nameof(TaskController));
            IServiceCollection serviceCollection = services.AddSingleton<ActivitySource>(source);
            return services;
        }

        public static IServiceCollection SetupFacade(this IServiceCollection services)
        {
            services.AddSingleton<ITaskFacade, TaskFacade>();
            return services;
        }

        public static IServiceCollection SetupDonationClient(this IServiceCollection services, ISettingsProvider settingsProvider)
        {
            var donationClient = new DonationClient(settingsProvider.DonationServiceUrl);
            services.AddSingleton<IDonationClient>(donationClient);
            return services;
        }
    }
}
