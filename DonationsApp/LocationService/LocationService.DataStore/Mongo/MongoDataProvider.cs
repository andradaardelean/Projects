using System.Linq;
using System.Linq.Expressions;
using LocationService.Models.Entities;
using MongoDB.Driver;
using MongoDB.Driver.Linq;

namespace LocationService.DataStore.Mongo
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

        protected IMongoCollection<Center> Collection => _context.Database.GetCollection<Center>(_collectionName);

        public async Task<List<Center>> GetAllAsync(Expression<Func<Center, bool>> match)
        {
            var centers = await Collection.Find(match).ToListAsync();
            return centers;
        }

        public async Task<Center> GetAsync(Expression<Func<Center, bool>> match)
        {
            var user = await Collection.AsQueryable()
                .Where(match)
                .FirstOrDefaultAsync();
            return user;
        }

        public async Task InsertAsync(Center user)
        {
            await Collection.InsertOneAsync(user);
        }
    }
}
