class queryGraphql:
     
      def __init__(self ):
      
           self.query_01 ="""{
  allOpportunityApplication(per_page: 2000,filters:  {created_at: {from:"2019-07-01T00:00:01Z", to:"2019-07-15T23:59:59Z"},person_home_mc:1606}) 
    {
    paging {
      total_pages
      current_page
      total_items
    }
    data {
      id
      status
      created_at
      date_matched
      date_approved
      date_realized
      experience_start_date
      experience_end_date
      date_approval_broken
      nps_response_completed_at
      updated_at
      person {
        id
        home_mc {
          id
          name
        }
        home_lc {
          id
          name
        }
      }
      host_lc {
        id
        name
      }
      home_mc {
        id
        name
      }
      opportunity {
        id
				created_at
        title
        available_openings
        duration
        
        sub_product{
          name
        }
        programme {
          id
          short_name_display
        }
      }
      standards {
        option
      }
    }
  }
}
              """      
      def chamaGraphQL(self):
              input_query = self.query_01 
              return  input_query
pass