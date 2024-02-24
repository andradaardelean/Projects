using System.Linq.Expressions;
using MongoDB.Driver;
using MongoDB.Driver.Linq;
using TaskService.Models.Entities;

namespace TaskService.DataStore.Mongo
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

        protected IMongoCollection<DonationTask> Collection => _context.Database.GetCollection<DonationTask>(_collectionName);

        public async Task<List<DonationTask>> GetAllAsync(Expression<Func<DonationTask, bool>> match)
        {
            var centers = await Collection.Find(match).ToListAsync();
            return centers;
        }

        public async Task<DonationTask> GetAsync(Expression<Func<DonationTask, bool>> match)
        {
            var user = await Collection.AsQueryable()
                .Where(match)
                .FirstOrDefaultAsync();
            return user;
        }

        public async Task InsertAsync(DonationTask user)
        {
            await Collection.InsertOneAsync(user);
        }

        public async Task UpdateAsync(DonationTask donationTask)
        {
            await Collection.DeleteOneAsync(task => task.Id == donationTask.Id);
            await InsertAsync(donationTask);
        }
    }
}
