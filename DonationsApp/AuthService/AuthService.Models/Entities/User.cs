using MongoDB.Bson;
using MongoDB.Bson.Serialization.Attributes;

namespace AuthService.Models.Entities
{
    public enum UserType
    {
        Employee,
        User
    }
    public class User
    {
        [BsonElement("_id")]
        [BsonId]
        [BsonRepresentation(BsonType.ObjectId)]
        public string Id { get; set; }
        public string FirstName { get; set; }
        public string LastName { get; set; }
        public string Email { get; set; }
        public string Password { get; set; }
        public UserType Type { get; set; }

        public override string? ToString()
        {
            return $"Id: {Id}, FirstName: {FirstName}, LastName: {LastName}, Email: {Email}, Password: {Password}, Type: {Type}";
        }
    }

}
