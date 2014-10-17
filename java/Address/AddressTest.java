public class AddressTest {
   public static class Name {
      private String surname = null;
      private String firstname = null;

      public Name() {
      }

      public Name(Name n) {
         this.surname = n.surname;
         this.firstname = n.firstname;
      }

      public static Object parse(String s) {
         Name n = new Name();
         String[] arr = s.split(" ");
         if (arr.length == 2) {
            n.setFirstname(arr[0]);
            n.setSurname(arr[1]);
         }
         return n;
      }

      @Override
      public String toString() {
         return this.firstname + " " + this.surname;
      }

      public String getSurname() {
         return surname;
      }

      public void setSurname(String surname) {
         this.surname = surname;
      }

      public String getFirstname() {
         return firstname;
      }

      public void setFirstname(String firstname) {
         this.firstname = firstname;
      }
   }

   private int streetNo = 0;
   private String street = null;
   private String city = null;
   private int postcode = 0;
   private String state = null;
   private Name name = null;

   public AddressTest() {
      super();
   }

   public AddressTest(Integer streetNo, String street, String city, int postcode,
     String state) {
      super();
      setAddress(streetNo, street, city, postcode, state);
   }

   public void setAddress(Integer streetNo, String street, String city,
     int postcode, String state) {
      this.streetNo = streetNo.intValue();
      this.street = street;
      this.city = city;
      this.postcode = postcode;
      this.state = state;
   }

   protected void setStreetNo(Integer streetNo) {
      this.streetNo = streetNo;
   }

   public Integer getStreetNo() {
      return this.streetNo;
   }

   public String getStreet() {
      return this.street;
   }

   public void setCity(String city) {
      this.city = city;
   }

   public String getCity() {
      return this.city;
   }

   public void setPostcode(int postcode) {
      this.postcode = postcode;
   }

   public int getPostcode() {
      return this.postcode;
   }

   public String getFullAddress() {
      return this.streetNo + " " + this.street + ", " + this.city + ", "
        + this.state + " - " + this.postcode;
   }

   public void setStreet(String street) {
      this.street = street;
   }

   public String getState() {
      return this.state;
   }

   public void setState(String state) {
      this.state = state;
   }

   public Name getName() {
      return this.name;
   }

   public void setName(Name name) {
      this.name = name;
   }
}
