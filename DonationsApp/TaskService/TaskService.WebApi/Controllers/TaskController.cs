using Microsoft.AspNetCore.Mvc;
using System.Net.Mime;
using TaskService.Models.Entities;
using TaskService.Models.Requests;
using TaskService.WebApi.Services;

namespace TaskService.WebApi.Controllers
{
    [ApiController]
    [Route("task")]
    [Produces(MediaTypeNames.Application.Json)]
    public class TaskController : ControllerBase
    {
        private readonly ITaskFacade _taskFacade;

        public TaskController(ITaskFacade taskFacade)
        {
            _taskFacade = taskFacade;
        }

        /// <summary>
        /// Add task.
        /// </summary>
        /// <response code="200">Create task request.</response>
        [HttpPost]
        [Route("addTask")]
        [Consumes(MediaTypeNames.Application.Json)]
        [ProducesResponseType(StatusCodes.Status200OK)]
        public async Task AddTask(AddTaskRequest request)
        {

            await _taskFacade.AddTask(request.DonationId);
        }

        /// <summary>
        /// Get all tasks by status.
        /// </summary>
        /// <response code="200">Get all task.</response>
        [HttpPost]
        [Route("get")]
        [Consumes(MediaTypeNames.Application.Json)]
        [ProducesResponseType(StatusCodes.Status200OK)]
        public async Task<List<DonationTaskWithDonation>> GetAllTasksByStatus(GetTasksAllByStatusRequest request)
        {
            return await _taskFacade.GetAllTasksForEmployee(request.EmployeeId, request.donationTaskStatus);
        }

        /// <summary>
        /// Get all tasks.
        /// </summary>
        /// <response code="200">Get all task.</response>
        [HttpPost]
        [Route("get/all")]
        [Consumes(MediaTypeNames.Application.Json)]
        [ProducesResponseType(StatusCodes.Status200OK)]
        public async Task<List<DonationTaskWithDonation>> GetAllTasks()
        {
            return await _taskFacade.GetAllCreatedTasks();
        }

        /// <summary>
        /// Update status for a task.
        /// </summary>
        /// <response code="200">Update status for a task.</response>
        [HttpPost]
        [Route("update")]
        [Consumes(MediaTypeNames.Application.Json)]
        [ProducesResponseType(StatusCodes.Status200OK)]
        public async Task UpdateStatus(UpdateStatusRequest request)
        {
            await _taskFacade.UpdateStatus(request.TaskId, request.EmployeeId, request.DonationTaskStatus);
        }
    }
}
