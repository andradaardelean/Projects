using MongoDB.Driver;

namespace LocationService.DataStore
{
    public interface IMongoDataContext
    {
        IMongoDatabase Database { get; }
    }
}