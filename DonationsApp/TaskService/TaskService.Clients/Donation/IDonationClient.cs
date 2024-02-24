using TaskService.Models.Entities;
using TaskService.Models.Requests;

namespace TaskService.Clients
{
    public interface IDonationClient
    {
        public Task<Donation> GetDonationById(GetDonationRequest request);
    }
}
