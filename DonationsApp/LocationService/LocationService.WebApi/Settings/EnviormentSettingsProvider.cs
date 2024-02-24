using System.Globalization;

namespace LocationService.WebApi.Settings
{
    public class EnvironmentVariablesSettingsProvider : ISettingsProvider
    {
        public string BindingAddress
        {
            get
            {
                return Environment.GetEnvironmentVariable("BINDING_ADRESS") ?? "http://localhost";
            }
        }

        public int Port
        {
            get
            {
                return int.Parse(Environment.GetEnvironmentVariable("BINDING_PORT") ?? "12600", CultureInfo.InvariantCulture);
            }
        }

        public string ConnectionString
        {
            get
            {
                return Environment.GetEnvironmentVariable("CONNECTION_STRING") ?? "mongodb://localhost:27017/santa";
            }
        }

        public string LocationCollection => "locations";

        public string JaegerHost
        {
            get
            {
                return Environment.GetEnvironmentVariable("JAEGER_AGENT_HOST") ?? "http://localhost";
            }
        }

        public string JaegerPort
        {
            get
            {
                return Environment.GetEnvironmentVariable("JAEGER_AGENT_PORT") ?? "16686";
            }
        }
    }
}
