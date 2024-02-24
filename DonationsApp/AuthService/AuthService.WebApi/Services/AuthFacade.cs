using AuthService.DataStore;
using AuthService.Models.Entities;
using System.Diagnostics;

namespace AuthService.WebApi.Services
{
    public class AuthFacade : IAuthFacade
    {
        private readonly IDataProvider _dataProvider;
        private readonly ActivitySource _source;

        public AuthFacade(IDataProvider dataProvider, ActivitySource source) {
            _dataProvider = dataProvider;
            _source = source;
        }

        public async Task<User> CreateAccount(string firstName, string lastName, string email, string password)
        {
            using var activity = _source.StartActivity("Create account");
            activity.AddTag("User", email);
            try
            {
                var user = new User()
                {
                    FirstName = firstName,
                    LastName = lastName,
                    Email = email,
                    Password = password,
                    Type = UserType.User
                };
                return await _dataProvider.InsertAsync(user);
            }
            catch (Exception ex)
            {
                activity.AddTag("Exception", ex.Message);
                return null;
            }

        }

        public async Task<User> GetUserById(string userId)
        {
            using var activity = _source.StartActivity("Get user by id");
            activity?.AddTag("UserID", userId);
            try
            {
                return await _dataProvider.GetAsync(user => user.Id == userId);
            }
            catch(Exception ex)
            {
                activity?.AddTag("Exception", ex.ToString());
                return null;
            }
        }

        public async Task<User> Login(string email,string password)
        {
            using var activity = _source.StartActivity("Login");
            activity?.AddTag("Email", email);
            activity?.AddTag("Password", password);
            try
            {
                return await _dataProvider.GetAsync(u => u.Email == email && u.Password == password);
            }
            catch(Exception ex)
            {
                activity?.AddTag("Exception", ex.Message);
                return null;
            }
        }
    }
}
