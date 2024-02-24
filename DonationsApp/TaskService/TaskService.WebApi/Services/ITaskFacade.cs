using TaskService.Models.Entities;

namespace TaskService.WebApi.Services
{
    public interface ITaskFacade
    {
        public Task AddTask(string DonationId);
        public Task UpdateStatus(string TaskId, string EmployeeId, DonationTaskStatus TaskStatus);
        public Task<List<DonationTaskWithDonation>> GetAllCreatedTasks();
        public Task<List<DonationTaskWithDonation>> GetAllTasksForEmployee(string employeeId, DonationTaskStatus status);
    }
}
