using AuthService.Models.Entities;
using System.Linq.Expressions;

namespace AuthService.DataStore
{
    public interface IDataProvider
    {
        Task<User> InsertAsync(User user);
        Task<User> GetAsync(Expression<Func<User, bool>> match);
    }
}
