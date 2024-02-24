using DonationService.Models.Entities;
using System.Linq.Expressions;

namespace DonationService.DataStore
{
    public interface IDataProvider
    {
        Task<Donation> InsertAsync(Donation Donation);
        Task<Donation> GetAsync(Expression<Func<Donation, bool>> match);
        Task<List<Donation>> GetAllAsync(Expression<Func<Donation, bool>> match);
    }
}
