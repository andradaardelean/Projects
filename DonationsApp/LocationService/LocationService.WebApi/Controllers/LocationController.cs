using Location.WebApi.Services;
using LocationService.Models.Entities;
using LocationService.Models.Requests;
using Microsoft.AspNetCore.Mvc;
using System.Net.Mime;

namespace LocationService.WebApi.Controllers
{
    [ApiController]
    [Route("location")]
    [Produces(MediaTypeNames.Application.Json)]
    public class LocationController : ControllerBase
    {
        private readonly ILocationFacade _locationFacade;

        public LocationController(ILocationFacade locationFacade)
        {
            _locationFacade = locationFacade;
        }

        /// <summary>
        /// Add locatin.
        /// </summary>
        /// <response code="200">Create account request.</response>
        [HttpPost]
        [Route("addCenter")]
        [Consumes(MediaTypeNames.Application.Json)]
        [ProducesResponseType(StatusCodes.Status200OK)]
        public async Task AddCenter(AddCenterRequest request)
        {

            await _locationFacade.AddCenter(request.City, request.State, request.Name, request.Address);
        }

        /// <summary>
        /// Get all centers.
        /// </summary>
        /// <response code="200">Get all center request.</response>
        [HttpPost]
        [Route("getCenters")]
        [Consumes(MediaTypeNames.Application.Json)]
        [ProducesResponseType(StatusCodes.Status200OK)]
        public async Task<List<Center>> GetCenters(GetCentersRequest request)
        {

            return await _locationFacade.GetAllCenterByCityAndState(request.City, request.State);
        }

        /// <summary>
        /// Get all cities.
        /// </summary>
        /// <response code="200">Get all cities request.</response>
        [HttpPost]
        [Route("getCities")]
        [Consumes(MediaTypeNames.Application.Json)]
        [ProducesResponseType(StatusCodes.Status200OK)]
        public async Task<List<string>> GetCities(GetCitiesRequest request)
        {

            return await _locationFacade.GetAllCitiesByState(request.State);
        }

        /// <summary>
        /// Get all states.
        /// </summary>
        /// <response code="200">Get all states request.</response>
        [HttpPost]
        [Route("getStates")]
        [Consumes(MediaTypeNames.Application.Json)]
        [ProducesResponseType(StatusCodes.Status200OK)]
        public async Task<List<string>> GetStates()
        {

            return await _locationFacade.GetAllStates();
        }
    }
}
