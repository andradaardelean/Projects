using TaskService.Models.Entities;

namespace TaskService.Models.Requests
{
    public class UpdateStatusRequest
    {
        public string TaskId { get; set; }
        public string EmployeeId { get; set; }
        public DonationTaskStatus DonationTaskStatus { get; set; }
    }
}
