using AuthService.Models.Entities;
using AuthService.Models.Requests;
using AuthService.WebApi.Services;
using Microsoft.AspNetCore.Cors;
using Microsoft.AspNetCore.Mvc;
using System.Net.Mime;

namespace AuthService.WebApi.Controllers
{
    [ApiController]
    [Route("auth")]
    [Produces(MediaTypeNames.Application.Json)]
    public class AuthController : ControllerBase
    {
        private readonly IAuthFacade _authFacade;

        public AuthController(IAuthFacade authFacade)
        {
            _authFacade = authFacade;
        }

        private void setUserIdCookie(string userId)
        {
            HttpContext.Response.Cookies.Append("userId", userId, new CookieOptions { SameSite = SameSiteMode.Lax, Secure = false});
        }

        /// <summary>
        /// Create account request.
        /// </summary>
        /// <response code="200">Create account request.</response>
        [HttpPost]
        [Route("createAccount")]
        [Consumes(MediaTypeNames.Application.Json)]
        [ProducesResponseType(StatusCodes.Status200OK)]
        public async Task CreateAccount(CreateAccountRequest request)
        {
            var user = await _authFacade.CreateAccount(request.FirstName, request.LastName, request.Email, request.Password);
            setUserIdCookie(user.Id);
        }

        /// <summary>
        /// Login request.
        /// </summary>
        /// <response code="200">Login.</response>
        [HttpPost]
        [Route("login")]
        [Consumes(MediaTypeNames.Application.Json)]
        [ProducesResponseType(StatusCodes.Status200OK)]
        [ProducesResponseType(StatusCodes.Status404NotFound)]
        public async Task<ActionResult<User>> Login(LoginRequest request)
        {
            var user = await _authFacade.Login(request.Email, request.Password);

            if (user == null)
            {
                return NotFound();
            }

            setUserIdCookie(user.Id);
            return user;
        }


        /// <summary>
        /// Get logged user.
        /// </summary>
        /// <response code="200">Get logged user.</response>
        [HttpPost]
        [Route("loggedUser")]
        [Consumes(MediaTypeNames.Application.Json)]
        [ProducesResponseType(StatusCodes.Status200OK)]
        [ProducesResponseType(StatusCodes.Status404NotFound)]
        public async Task<ActionResult<User>> GetLoggedUser()
        {
            if (!HttpContext.Request.Cookies.TryGetValue("userId", out string? userId))
            {
                return NotFound();
            }

            var user = await _authFacade.GetUserById(userId);
            if (user == null)
            {
                return NotFound();
            }

            return Ok(user);
        }

    }
}
