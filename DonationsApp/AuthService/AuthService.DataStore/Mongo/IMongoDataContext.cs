using MongoDB.Driver;

namespace AuthService.DataStore
{
    public interface IMongoDataContext
    {
        IMongoDatabase Database { get; }
    }
}