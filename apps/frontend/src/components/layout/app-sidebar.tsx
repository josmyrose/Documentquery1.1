import { Card } from "@/components/ui/card";

type AppSidebarProps = {
  children: React.ReactNode;
};

export function AppSidebar({ children }: AppSidebarProps) {
  return (
    <div className="space-y-6">
      <Card className="overflow-hidden">
        <div className="flex items-center gap-3">
          <div className="flex h-11 w-11 items-center justify-center rounded-2xl bg-slate-900 text-sm font-bold text-white">
            DQ
          </div>
          <div>
            <h1 className="text-lg font-semibold text-slate-900">DocuQuery AI</h1>
            <p className="text-sm text-slate-500">
              Document intelligence workspace
            </p>
          </div>
        </div>
      </Card>

      {children}
    </div>
  );
}