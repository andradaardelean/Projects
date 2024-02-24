
using DonationService.Models.Entities;
using DonationService.Models.Requests;
using DonationService.WebApi.Services;
using Microsoft.AspNetCore.Mvc;
using System.Net.Mime;

namespace DonationService.WebApi.Controllers
{
    [ApiController]
    [Route("donation")]
    [Produces(MediaTypeNames.Application.Json)]
    public class DonationController : ControllerBase
    {
        private readonly IDonationFacade _donationFacade;

        public DonationController(IDonationFacade locationFacade)
        {
            _donationFacade = locationFacade;
        }

        /// <summary>
        /// Add donation.
        /// </summary>
        /// <response code="200">Create donation request.</response>
        [HttpPost]
        [Route("addDonation")]
        [Consumes(MediaTypeNames.Application.Json)]
        [ProducesResponseType(StatusCodes.Status200OK)]
        public async Task AddDonation(AddDonationRequest request)
        {

            await _donationFacade.AddDonation(request.CenterId, request.ChildGroup, request.Donator, request.GiftDescription);
        }

        /// <summary>
        /// Get donation.
        /// </summary>
        /// <response code="200">Get donnation by id request.</response>
        [HttpPost]
        [Route("get")]
        [Consumes(MediaTypeNames.Application.Json)]
        [ProducesResponseType(StatusCodes.Status200OK)]
        public async Task<Donation> GetDonation(GetDonationRequest request)
        {

            return await _donationFacade.GetDonationById(request.DonationId);
        }
    }
}
