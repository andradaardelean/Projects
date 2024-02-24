using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace TaskService.Models.Entities
{
    public enum DonationTaskStatus
    {
        Created,
        Pending,
        Completed
    }
    public class DonationTask
    {
        [BsonElement("_id")]
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string Id { get; set; }
        public string DonationId { get; set; }
        public string EmployeeId { get; set; }
        public DonationTaskStatus DonationTaskStatus { get; set; }
    }
}
