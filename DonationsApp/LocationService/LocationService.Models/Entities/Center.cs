using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace LocationService.Models.Entities
{
    public class Center
    {
        [BsonElement("_id")]
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string Id { get; set; }
        public string State { get; set; }
        public string City { get; set; }
        public string Name { get; set; }
        public string Address { get; set; }

        public override string? ToString()
        {
            return $"State: {State}, City: {City}, Name: {Name}, Adress: {Address}";
        }
    }
}
