
using MongoDB.Driver;

namespace TaskService.DataStore
{
    public interface IMongoDataContext
    {
        IMongoDatabase Database { get; }
    }
}