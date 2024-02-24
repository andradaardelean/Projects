namespace DonationService.WebApi.Settings
{
    public interface ISettingsProvider
    {
        string BindingAddress { get; }
        int Port { get; }
        string ConnectionString { get; }
        string DonationCollection { get; }
        string TaskServiceUrl { get; }
        string JaegerHost { get; }
        string JaegerPort { get; }
    }
}
