

using DonationService.Clients.Donation;
using DonationService.DataStore;
using DonationService.Models.Entities;
using System.Diagnostics;
using TaskService.Models.Requests;

namespace DonationService.WebApi.Services
{
    public class DonationFacade : IDonationFacade
    {
        private readonly IDataProvider _dataProvider;
        private readonly ActivitySource _source;
        private readonly ITaskClient _taskClient;

        public DonationFacade(IDataProvider dataProvider, ITaskClient taskClient, ActivitySource source) {
            _dataProvider = dataProvider;
            _taskClient = taskClient;
            _source = source;
        }

        public async Task AddDonation(string centerId,ChildGroup childGroup, Donator donator, string giftDescription)
        {
            using var activity = _source.StartActivity("Add donation");
            activity?.SetTag("donation", centerId);
            try
            {
                var donation = new Donation()
                {
                    CenterId = centerId,
                    ChildGroup = childGroup,
                    Donator = donator,
                    GiftDescription = giftDescription
                };
                var donatonInserted = await _dataProvider.InsertAsync(donation);
                var request = new AddTaskRequest()
                {
                    DonationId = donatonInserted.Id
                };
                await _taskClient.CreateTask(request);
            }
            catch (Exception ex)
            {
                activity?.SetTag("Exception", ex.Message);
            }
        }

        public async Task<Donation> GetDonationById(string donationId)
        {
            using var activity = _source.StartActivity("Get donation by id");
            activity?.AddTag("DonationId:", donationId);
            try
            {
                return await _dataProvider.GetAsync(donation => donation.Id == donationId);
            }
            catch (Exception ex)
            {
                Console.WriteLine(ex.Message);
                activity?.AddTag("Exception:", ex.Message.ToString());
                return null;
            }
        }
    }
}
