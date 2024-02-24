using TaskService.Models.Requests;

namespace DonationService.Clients.Donation
{
    public interface ITaskClient
    {
        Task CreateTask(AddTaskRequest request);
    }
}
