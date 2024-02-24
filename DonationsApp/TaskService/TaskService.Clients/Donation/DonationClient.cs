using TaskService.Models.Entities;
using TaskService.Models.Requests;

namespace TaskService.Clients
{
    public class DonationClient : BaseClient, IDonationClient
    {
        public DonationClient(string baseUrl) : base(baseUrl)
        {
        }

        public async Task<Donation> GetDonationById(GetDonationRequest request)
        {
            try
            {
                var url = BaseUrl + "/donation/get";
                var response =  await PostAsync(url, request);
                return await DeserializeResponseContentAsync<Donation>(response);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                return null;
            }
        }
    }
}
