using DonationService.Models.Entities;

namespace DonationService.Models.Requests
{
    public class AddDonationRequest
    {
        public string CenterId { get; set; }
        public ChildGroup ChildGroup { get; set; }
        public Donator Donator { get; set; }
        public string GiftDescription { get; set; }
    }
}
