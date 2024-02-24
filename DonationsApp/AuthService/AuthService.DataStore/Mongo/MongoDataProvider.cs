using System.Linq.Expressions;
using AuthService.Models.Entities;
using MongoDB.Driver;
using MongoDB.Driver.Linq;

namespace AuthService.DataStore.Mongo
{
    public class MongoDataProvider : IDataProvider
    {
        private readonly IMongoDataContext _context;
        private readonly string _collectionName;

        public MongoDataProvider(IMongoDataContext context, string collectionName)
        {
            _context = context ?? throw new ArgumentNullException(nameof(context));
            _collectionName = collectionName ?? throw new ArgumentNullException(nameof(collectionName));
        }

        protected IMongoCollection<User> Collection => _context.Database.GetCollection<User>(_collectionName);

        public async Task<User> GetAsync(Expression<Func<User, bool>> match)
        {
            var user = await Collection.AsQueryable()
                .Where(match)
                .FirstOrDefaultAsync();
            return user;
        }

        public async Task<User> InsertAsync(User user)
        {
            await Collection.InsertOneAsync(user);
            return user;
        }
    }
}
