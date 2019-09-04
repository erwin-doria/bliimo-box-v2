const downloadEvents = () => {
  new Ping().ping('https://google.com', async function(err, data) {
    if (!err) {
      $('#bg-main').show();
      $('#bg-main').css('z-index', '999999');
      $('#load-events').show();

      const data = JSON.parse(
        await request(
          'POST',
          '/events',
          {},
          { Authorization: getStorage('Authorization') }
        )
      );

      setEvents(data);

      setTimeout(() => {
        $('#load-events').hide();
        $('#bg-main').hide();
        $('#bg-main').css('z-index', '-1');
      }, 1000);
    } else {
      alert('No internet connection');
    }
  });
};

const setEvents = data => {
  const row = $('.events-row');
  row.empty();
  events = '';

  if (data.length > 0) {
    Object.keys(data).map(i => {
      events += `<div class="col-md-4 col-lg-3">
                        <a href="/events/${
                          data[i]['id']
                        }" class="text-dark text-decoration-0 events-btn">
                            <div class="card">
                                <div class="card-header ellipsis" data-ellipsis="1">${
                                  data[i]['title']
                                }</div>
                                <div class="card-body">
                                    <div class="card-text ellipsis" data-ellipsis="5">${
                                      data[i]['description']
                                    }
                                    </div>
                                    <p class=" text-right events-date">
                                    '--- --, --'
                                    </p>
                                </div>
                            </div>
                        </a>
                    </div>`;
    });
    $('.search').removeClass('d-none');
  }

  if (events.length == 0) {
    events = `<div class="col-12 text-center">
                  <h4 class="font-weight-bold">No events found.</h4>
              </div>`;
  }

  row.append(events);
};

const searchEvents = async search => {
  console.log(search);
  const data = JSON.parse(await request('POST', '/events/search', { search }));
  setEvents(data);
};

$(document).ready(function() {
  $('#bg-main').hide();
  $('#search').on('keyup', function(e) {
    searchEvents($(this).val());
  });
});
