using TaskService.Models.Entities;

namespace TaskService.Models.Requests
{
    public class GetTasksAllByStatusRequest
    {
        public string EmployeeId { get; set; }
        public DonationTaskStatus donationTaskStatus { get; set; }
    }
}
