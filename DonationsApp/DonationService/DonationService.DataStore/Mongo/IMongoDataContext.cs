
using MongoDB.Driver;

namespace DonationService.DataStore
{
    public interface IMongoDataContext
    {
        IMongoDatabase Database { get; }
    }
}