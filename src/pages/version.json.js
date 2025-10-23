export async function GET() {
  const response = await fetch(
    'https://api.github.com/repos/swiftDialog/swiftDialog/releases/latest'
  );
  
  const data = await response.json();
  
  return new Response(JSON.stringify({
    version: data.tag_name.replace(/^v/, ''),
    released: data.published_at
  }), {
    headers: { 'Content-Type': 'application/json' }
  });
}

export const prerender = true; // This makes it build-time only