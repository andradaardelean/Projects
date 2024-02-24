using LocationService.Models.Entities;
using System.Linq.Expressions;

namespace LocationService.DataStore
{
    public interface IDataProvider
    {
        Task InsertAsync(Center center);
        Task<Center> GetAsync(Expression<Func<Center, bool>> match);
        Task<List<Center>> GetAllAsync(Expression<Func<Center, bool>> match);
    }
}
