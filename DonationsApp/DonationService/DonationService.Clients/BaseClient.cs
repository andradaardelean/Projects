using System.Net.Http.Json;
using System.Text.Json;

namespace DonationService.Clients
{
    public class BaseClient
    {
        private readonly string _baseUrl;
        private readonly HttpClient _httpClient;
        public BaseClient(string baseUrl)
        {
            _baseUrl = baseUrl;
            _httpClient = new HttpClient();
        }

        public string BaseUrl { get => _baseUrl; }
        public HttpClient HttpClient { get => _httpClient; }

        public static async Task<T> DeserializeResponseContentAsync<T>(HttpResponseMessage response) where T : class
        {
            var body = await response.Content.ReadAsStringAsync();
            return Deserialize<T>(body);
        }

        private static T Deserialize<T>(string json) where T : class
        {
            if (string.IsNullOrEmpty(json))
            {
                return null;
            }
            return JsonSerializer.Deserialize<T>(json, new JsonSerializerOptions
            {
                PropertyNameCaseInsensitive = true
            });
        }

        public async Task<HttpResponseMessage> PostAsync(string url, object body = null)
        {
            return await HttpClient.PostAsJsonAsync(url, body, new JsonSerializerOptions
            {
                PropertyNameCaseInsensitive = true
            });
        }
    }
}