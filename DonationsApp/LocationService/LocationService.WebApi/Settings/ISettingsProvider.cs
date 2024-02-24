namespace LocationService.WebApi.Settings
{
    public interface ISettingsProvider
    {
        string BindingAddress { get; }
        int Port { get; }
        string ConnectionString { get; }
        string LocationCollection { get; }
        string JaegerHost { get; }
        string JaegerPort { get; }
    }
}
