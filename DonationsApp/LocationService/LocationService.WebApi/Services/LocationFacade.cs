
using Location.WebApi.Services;
using LocationService.DataStore;
using LocationService.Models.Entities;
using System.Diagnostics;

namespace LocationService.WebApi.Services
{
    public class LocationFacade : ILocationFacade
    {
        private readonly IDataProvider _dataProvider;
        private readonly ActivitySource _source;

        public LocationFacade(IDataProvider dataProvider, ActivitySource source) {
            _dataProvider = dataProvider;
            _source = source;
        }

        public async Task AddCenter(string city, string state, string name,string adress)
        {
            using var activity = _source.StartActivity("Add center");
            activity.AddTag("Center", name);
            try
            {
                var center = new Center()
                {
                    City = city,
                    State = state,
                    Name = name,
                    Address = adress
                };
                await _dataProvider.InsertAsync(center);
            }
            catch (Exception ex)
            {
                activity.AddTag("Exception", ex.Message);
            }
        }

        public async Task<List<Center>> GetAllCenterByCityAndState(string city, string state)
        {
            using var activity = _source.StartActivity("Get all centers by city and state");
            activity.AddTag("City", city);
            activity.AddTag("State", state);
            try
            {
                var centers = await _dataProvider.GetAllAsync(c => c.City == city && c.State == state);
                return centers;
            }
            catch (Exception ex)
            {
                activity.AddTag("Exception", ex.Message);
                return null;
            }
        }

        public async Task<List<string>> GetAllCitiesByState(string state)
        {
            using var activity = _source.StartActivity("Get all cities by state");
            activity.AddTag("State", state);
            try
            {
                var centers = await _dataProvider.GetAllAsync(c => c.State == state);

                var cities = new HashSet<string>();
                foreach(var center in centers)
                {
                    cities.Add(center.City);
                }

                return cities.ToList();
            }
            catch (Exception ex)
            {
                activity.AddTag("Exception", ex.Message);
                return null;
            }
        }

        public async Task<List<string>> GetAllStates()
        {
            using var activity = _source.StartActivity("Get all states");
            try
            {
                var centers = await _dataProvider.GetAllAsync(c => true);

                var states = new HashSet<string>();
                foreach (var center in centers)
                {
                    states.Add(center.State);
                }

                return states.ToList();
            }
            catch (Exception ex)
            {
                activity.AddTag("Exception", ex.Message);
                return null;
            }
        }
    }
}
