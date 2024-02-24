using System.Linq;
using System.Linq.Expressions;
using DonationService.Models.Entities;
using MongoDB.Driver;
using MongoDB.Driver.Linq;

namespace DonationService.DataStore.Mongo
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

        protected IMongoCollection<Donation> Collection => _context.Database.GetCollection<Donation>(_collectionName);

        public async Task<List<Donation>> GetAllAsync(Expression<Func<Donation, bool>> match)
        {
            var centers = await Collection.Find(match).ToListAsync();
            return centers;
        }

        public async Task<Donation> GetAsync(Expression<Func<Donation, bool>> match)
        {
            var user = await Collection.AsQueryable()
                .Where(match)
                .FirstOrDefaultAsync();
            return user;
        }

        public async Task<Donation> InsertAsync(Donation donation)
        {
            await Collection.InsertOneAsync(donation);

            return donation;
        }
    }
}
