namespace TaskService.Models.Entities
{
    public class DonationTaskWithDonation
    {
        public string Id { get; set; }
        public Donation Donation { get; set; }
        public string EmployeeId { get; set; }
        public DonationTaskStatus DonationTaskStatus { get; set; }
    }
}
