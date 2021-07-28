function main(splash, args)
  
  -- method 1 for changing user agent
  --splash:set_user_agent("Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36")
  
  -- method 2 for changing user agent
  --[[
  headers = {
    ["User-Agent"] = "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36"
  }
  splash:set_custom_headers(headers)
  ]]--
  
  -- method 3 for changing user agent
  splash:on_request(function(request)
      request:set_header('User-Agent', 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Mobile Safari/537.36')
  end)
  
  url = args.url
	assert(splash:go(url))
  assert(splash:wait(1))
  
  input_box = assert(splash:select("#search_form_input_homepage"))
  input_box:focus()
  input_box:send_text("my user agent")
  assert(splash:wait(0.5))
  
  -- clicking on a button (search in this case)
  --[[
  btn = assert(splash:select("#search_button_homepage"))
  btn:mouse_click()
  ]]--
  
  -- pressing the enter keystroke (within a search bar)
  input_box:send_keys("<Enter>")
  assert(splash:wait(5))
  
  splash:set_viewport_full()
  return {
    image = splash.png(),
    html = splash.html()
  }
end