require 'json'

def mask(value)
  return value.gsub(/([A-Za-z0-9._%+-]+)@([A-Za-z0-9.-]+\.[A-Za-z]{2,})/, '***@***')
end

event = {
  timestamp: Time.now.utc.iso8601,
  level: 'INFO',
  service_name: 'ruby-service',
  version: '0.0.1',
  trace_id: 'stub',
  message: 'hello from ruby',
  context: { email: mask('alice@example.com') }
}

puts JSON.generate(event)
