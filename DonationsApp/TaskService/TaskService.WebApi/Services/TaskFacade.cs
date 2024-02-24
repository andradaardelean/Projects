using OpenTelemetry.Resources;
using System.Diagnostics;
using System.Threading;
using TaskService.Clients;
using TaskService.DataStore;
using TaskService.Models.Entities;
using TaskService.Models.Requests;

namespace TaskService.WebApi.Services
{
    public class TaskFacade : ITaskFacade
    {
        private readonly IDataProvider _dataProvider;
        private readonly IDonationClient _donationClient;
        private readonly ActivitySource _source;


        public TaskFacade(IDataProvider dataProvider, IDonationClient donationClient, ActivitySource source)
        {
            _dataProvider = dataProvider;
            _donationClient = donationClient;
            _source = source;
        }

        public async Task AddTask(string donationId)
        {
            using var activity = _source.StartActivity("Add donationTask");
            activity?.SetTag("Donation Id", donationId);

            try
            {
                var donationTask = new DonationTask()
                {
                    DonationId = donationId,
                    DonationTaskStatus = DonationTaskStatus.Created
                };
                await _dataProvider.InsertAsync(donationTask);
            }
            catch (Exception ex)
            {
                activity?.SetTag("Exception", ex.Message);
            }
        }

        public async Task<List<DonationTaskWithDonation>> GetAllCreatedTasks()
        {
            using var activity = _source.StartActivity("Get all created tasks");
            try
            {
                var donationTasks =  await _dataProvider.GetAllAsync(task => task.DonationTaskStatus == DonationTaskStatus.Created);
                var list = new List<DonationTaskWithDonation>();
                foreach (var donationTask in donationTasks)
                {
                    var request = new GetDonationRequest()
                    {
                        DonationId = donationTask.DonationId
                    };
                    var donation = await _donationClient.GetDonationById(request);
                    var donationTaskWithDonation = new DonationTaskWithDonation()
                    {
                        Id = donationTask.Id,
                        Donation = donation,
                        EmployeeId = donationTask.EmployeeId,
                        DonationTaskStatus = donationTask.DonationTaskStatus
                    };
                    list.Add(donationTaskWithDonation);
                }
                return list;
            }
            catch (Exception ex)
            {
                activity?.SetTag("Exception", ex.Message);
                return new List<DonationTaskWithDonation>();
            }
        }

        public async Task<List<DonationTaskWithDonation>> GetAllTasksForEmployee(string employeeId, DonationTaskStatus status)
        {
            using var activity = _source.StartActivity("Get all tasks by status");
            try
            {
                var donationTasks =  await _dataProvider.GetAllAsync(task => task.DonationTaskStatus == status && task.EmployeeId == employeeId);
                var list = new List<DonationTaskWithDonation>();
                foreach (var donationTask in donationTasks)
                {
                    var request = new GetDonationRequest()
                    {
                        DonationId = donationTask.DonationId
                    };
                    var donation = await _donationClient.GetDonationById(request);
                    var donationTaskWithDonation = new DonationTaskWithDonation()
                    {
                        Id = donationTask.Id,
                        Donation = donation,
                        EmployeeId = donationTask.EmployeeId,
                        DonationTaskStatus = donationTask.DonationTaskStatus
                    };
                    list.Add(donationTaskWithDonation);
                }
                return list;
            }
            catch (Exception ex)
            {
                activity?.SetTag("Exception", ex.Message);
                return new List<DonationTaskWithDonation>();
            }
        }

        public async Task UpdateStatus(string taskId, string employeeId, DonationTaskStatus taskStatus)
        {
            using var activity = _source.StartActivity("Update Status");
            activity?.SetTag("Task id:", taskId);
            activity?.SetTag("Task status:", taskStatus);
            try
            {
                var donationTask = await _dataProvider.GetAsync(task => task.Id == taskId);
                donationTask.EmployeeId = employeeId;
                donationTask.DonationTaskStatus = taskStatus;
                await _dataProvider.UpdateAsync(donationTask);
            }
            catch (Exception ex)
            {
                activity?.SetTag("Exception", ex.Message);
            }
        }
    }
}
