using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace DonationService.Models.Entities
{
    [BsonIgnoreExtraElements]
    public class Donation
    {
        [BsonElement("_id")]
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string Id { get; set; }
        public string CenterId { get; set; }
        public ChildGroup ChildGroup { get; set; }
        public Donator Donator { get; set; }
        public string GiftDescription { get; set; }

        public override string? ToString()
        {
            return $"CenterId: {CenterId}, ChildGroup: {ChildGroup}, Donator: {Donator}, GiftDescription: {GiftDescription}";
        }
    }
}
