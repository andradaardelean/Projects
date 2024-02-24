using LocationService.Models.Entities;

namespace Location.WebApi.Services
{
    public interface ILocationFacade
    {
        Task AddCenter(string city, string state, string name, string adress);
        Task<List<string>> GetAllStates();
        Task<List<string>> GetAllCitiesByState(string state);
        Task<List<Center>> GetAllCenterByCityAndState(string city, string state);
    }
}
