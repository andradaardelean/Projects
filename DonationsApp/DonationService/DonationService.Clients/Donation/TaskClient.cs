using DonationService.Clients;
using DonationService.Clients.Donation;
using TaskService.Models.Requests;

namespace DonationService.Clients
{
    public class TaskClient : BaseClient, ITaskClient
    {
        public TaskClient(string baseUrl) : base(baseUrl)
        {
        }

        public async Task CreateTask(AddTaskRequest request)
        {
            try
            {
                var url = BaseUrl + "/task/addTask";
                var response = await PostAsync(url, request);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.ToString());
            }
        }
    }
}