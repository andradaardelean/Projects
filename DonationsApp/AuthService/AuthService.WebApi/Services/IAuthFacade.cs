using AuthService.Models.Entities;

namespace AuthService.WebApi.Services
{
    public interface IAuthFacade
    {
        Task<User> CreateAccount(string firstName, string lastName, string email, string password);

        Task<User> Login(string email,string password);

        Task<User> GetUserById(string userId);
    }
}
