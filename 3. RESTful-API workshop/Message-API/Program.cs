using Microsoft.EntityFrameworkCore;
using MessageAPI.Models;
using var client = new HttpClient();

var builder = WebApplication.CreateBuilder(args);

// Add services to the container.

builder.Services.AddControllers();
builder.Services.AddDbContext<MessageContext>(opt =>
    opt.UseInMemoryDatabase("Messages"));
builder.Services.AddSwaggerGen(c =>
{
   c.SwaggerDoc("v1", new() { Title = "MessageAPI", Version = "v1" });
});
builder.Services.AddLogging();

var app = builder.Build();

// Configure the HTTP request pipeline.
var ListOfMessages = await client.GetStringAsync("https://2022-nsmsa-phase-1-api.azurewebsites.net/api/message");

if (builder.Environment.IsDevelopment())
{
    //app.UseDeveloperExceptionPage();
}

app.UseSwagger();
app.UseSwaggerUI(c => c.SwaggerEndpoint("/swagger/v1/swagger.json", "MessageAPI v1"));
app.UseHttpsRedirection();

app.UseAuthorization();
app.UseHttpLogging();

app.MapControllers();

app.Run();