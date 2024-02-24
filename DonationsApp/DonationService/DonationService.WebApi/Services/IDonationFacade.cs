
using DonationService.Models.Entities;

namespace DonationService.WebApi.Services
{
    public interface IDonationFacade
    {
        Task AddDonation(string centerId, ChildGroup childGroup, Donator donator, string giftDescription);
        Task<Donation> GetDonationById(string donationId);
    }
}
