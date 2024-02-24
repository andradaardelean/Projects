using System.Linq.Expressions;
using TaskService.Models.Entities;

namespace TaskService.DataStore
{
    public interface IDataProvider
    {
        Task InsertAsync(DonationTask task);
        Task<DonationTask> GetAsync(Expression<Func<DonationTask, bool>> match);
        Task<List<DonationTask>> GetAllAsync(Expression<Func<DonationTask, bool>> match);
        Task UpdateAsync(DonationTask donationTask);
    }
}
