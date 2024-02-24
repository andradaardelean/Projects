namespace TaskService.WebApi.Settings
{
    public interface ISettingsProvider
    {
        string BindingAddress { get; }
        int Port { get; }
        string ConnectionString { get; }
        string TaskCollection { get; }
        string DonationServiceUrl { get; }
        string JaegerHost { get; }
        string JaegerPort { get; }
    }
}
